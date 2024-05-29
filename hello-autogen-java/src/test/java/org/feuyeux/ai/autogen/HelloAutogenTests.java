package org.feuyeux.ai.autogen;

import com.hw.autogen4j.agent.AssistantAgent;
import com.hw.openai.OpenAiClient;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static com.hw.autogen4j.entity.HumanInputMode.NEVER;

@SpringBootTest
@Slf4j
class HelloAutogenTests {

    public static final String URL = "http://0.0.0.0:4000";
    public static final String API_KEY = "NotRequired";

    @Test
    public void test() {
        var cathy = AssistantAgent.builder()
                .client(OpenAiClient.builder()
                        .openaiApiBase(URL)
                        .openaiApiKey(API_KEY)
                        .build().init())
                .name("cathy")
                .systemMessage("Your name is Cathy and you are a part of a duo of comedians.")
                .humanInputMode(NEVER)
                .build();
        var joe = AssistantAgent.builder()
                .client(OpenAiClient.builder()
                        .openaiApiBase(URL)
                        .openaiApiKey(API_KEY)
                        .build().init())
                .name("joe")
                .systemMessage("Your name is Joe and you are a part of a duo of comedians.")
                .humanInputMode(NEVER)
                .build();
        joe.initiateChat(cathy, "Cathy, 来个段子，要高级，不许谐音梗哦");
    }
}
