#根據鍾誠老師的groqHello.py改寫,有借助chatgpt幫忙
import os
from groq import Groq

# 设置环境变量
os.environ["GROQ_API_KEY"] = "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"

# 获取API key
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("The GROQ_API_KEY environment variable is not set")

# 创建Groq客户端
client = Groq(api_key=api_key)

def chat_with_groq():
    conversation_history = [
        {"role": "system", "content": "你是一個會用中文回答問題的助手。"}  # 初始訊息,讓他用中文回答(不然有時候聊著就變英文回答了)
    ]
    
    while True:   #可以一直聊,直到出現退出等句子
        user_input = input("你: ")
        if user_input.lower() in ['退出', 'bye', '再見']:
            print("聊天機器人: 再見！")
            break
        
        conversation_history.append({"role": "user", "content": user_input})  #留下歷史紀錄
        
        # 创建聊天完成请求
        chat_completion = client.chat.completions.create(
            messages=conversation_history,  
            model="llama3-8b-8192",  #模型
        ) 
        
        response = chat_completion.choices[0].message.content
        print("聊天機器人: " + response)   #印出回應
        
        conversation_history.append({"role": "assistant", "content": response})  #留下歷史紀錄

if __name__ == "__main__":
    chat_with_groq()

