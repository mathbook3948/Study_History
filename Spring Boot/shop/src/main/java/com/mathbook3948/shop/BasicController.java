package com.mathbook3948.shop;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class BasicController {
    @GetMapping("/")
    @ResponseBody
    String hello() {
        return "안녕하세요";
    }

    @GetMapping("/about")
    @ResponseBody
    String about() {
        return "피싱사이트에요";
    }
}
