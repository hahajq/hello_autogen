package org.feuyeux.ai.autogen;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@Slf4j
public class HelloAutogen {
  public static void main(String[] args) {
    SpringApplication springApplication = new SpringApplication(HelloAutogen.class);
    springApplication.setBannerMode(Banner.Mode.OFF);
    springApplication.run(args);
  }
}
