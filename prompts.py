system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


### Sample Response Object ###
## ChatCompletion(
#    id='gen-8888888888-********************', 
#    choices=[
#        Choice(
#            finish_reason='stop', 
#            index=0, 
#            logprobs=None, 
#            message=ChatCompletionMessage(
#                content="I'M JUST A ROBOT", 
#                refusal=None, 
#                role='assistant', 
#                annotations=None, 
#                audio=None, 
#                function_call=None, 
#                tool_calls=None, 
#                reasoning=None
#                ), 
#            native_finish_reason='stop'
#            )
#        ], 
#    created=1788566231, 
#    model='minimax/minimax-m3:free', 
#    object='chat.completion', 
#    moderation=None, 
#    service_tier=None, 
#    system_fingerprint=None, 
#    usage=CompletionUsage(
#        completion_tokens=7, 
#        prompt_tokens=181, 
#        total_tokens=188, 
#        completion_tokens_details=CompletionTokensDetails(
#            accepted_prediction_tokens=None, 
#            audio_tokens=0, 
#            reasoning_tokens=0, 
#            rejected_prediction_tokens=None, 
#            image_tokens=0
#            ), 
#        prompt_tokens_details=PromptTokensDetails(
#            audio_tokens=0, 
#            cached_tokens=128, 
#            cache_write_tokens=0, 
#            video_tokens=0
#            ), 
#        cost=0, 
#        is_byok=False, 
#        cost_details={
#            'upstream_inference_cost': 0, 
#            'upstream_inference_prompt_cost': 0, 
#            'upstream_inference_completions_cost': 0
#            }
#        ), 
#    provider='GMICloud'
#)
######

