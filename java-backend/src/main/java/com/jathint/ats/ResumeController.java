package com.jathint.ats;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ResumeController {
    @PostMapping("/upload")
    public String uploadResume(@RequestParam("file") MultipartFile file) {
        return "File received: " + file.getOriginalFilename();
    }
}