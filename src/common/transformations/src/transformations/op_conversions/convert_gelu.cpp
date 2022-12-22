// Copyright (C) 2018-2022 Intel Corporation
// SPDX-License-Identifier: Apache-2.0
//

#include <memory>
#include <ngraph/ngraph.hpp>
#include <ngraph/pattern/op/wrap_type.hpp>
#include <ngraph/rt_info.hpp>
#include <openvino/opsets/opset1.hpp>
#include <openvino/opsets/opset2.hpp>
#include <transformations/op_conversions/convert_gelu.hpp>

#include "itt.hpp"

ov::pass::ConvertGELU::ConvertGELU() {
    MATCHER_SCOPE(ConvertGELU);
    auto gelu = pattern::wrap_type<ov::opset2::Gelu>();

    matcher_pass_callback callback = [this](pattern::Matcher& m) {
        auto gelu = std::dynamic_pointer_cast<ov::opset2::Gelu>(m.get_match_root());
        if (!gelu || transformation_callback(gelu))
            return false;
        auto input = gelu->input_value(0);
        auto input_type = input.get_element_type();

        // f(x) = 0.5 * x * (1.0 + erf( x / sqrt(2.0) )
        auto mul =
            std::make_shared<ov::opset1::Multiply>(input, ov::opset1::Constant::create(input_type, Shape{}, {0.5}));
        auto sq2 = std::make_shared<ov::opset1::Sqrt>(ov::opset1::Constant::create(input_type, Shape{}, {2.0}));
        auto div = register_new_node<ov::opset1::Divide>(input, sq2);  // can be decomposed
        auto erf = std::make_shared<ov::opset1::Erf>(div);
        auto add = std::make_shared<ov::opset1::Add>(erf, ov::opset1::Constant::create(input_type, Shape{}, {1.0}));
        auto res = std::make_shared<ov::opset1::Multiply>(mul, add);

        res->set_friendly_name(gelu->get_friendly_name());
        ngraph::copy_runtime_info(gelu, {mul, sq2, div, erf, add, res});
        ngraph::replace_node(gelu, res);
        return true;
    };

    auto m = std::make_shared<ngraph::pattern::Matcher>(gelu, matcher_name);
    register_matcher(m, callback, PassProperty::CHANGE_DYNAMIC_STATE);
}
