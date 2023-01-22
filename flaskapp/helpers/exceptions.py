class IllegalContentError(Exception):
    def __init__(self, response_obj):
        self.__message = self.__create_message(response_obj)
        super().__init__(self.__message)

    @property
    def message(self):
        return self.__message

    def __create_message(self, response_obj):
        reasons = []
        for reason, flag in response_obj["results"][0]["categories"].items():
            if flag:
                reasons.append(f"\t{str(reason)}")
        
        message = "This request contains abusive content. Your request was rejected for the following reason(s):\n" +\
            "\n".join(reasons) +\
            "\n" +\
            "Refer to OpenAI's content policy: https://beta.openai.com/docs/usage-policies/content-policy"

        return message
