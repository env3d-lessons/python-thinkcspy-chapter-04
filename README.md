# Python Loops – Chapter 4 

## Introduction

You've probably heard the term **Large Language Model** (or **LLM**).
A *large language model* is a type of artificial intelligence trained to understand and generate human-like text. It's the kind of model that powers tools like ChatGPT.

In this exercise, we’ll use the same prompt to focus on how the temperature setting impacts the responses of the LLM. 
This will help you observe variations in tone, creativity, and content.

I'm providing you with a function called `chat` that lets you interact with an LLM. The function takes two inputs:

1. A **prompt** (a string you want to ask or say to the LLM), and
2. A **temperature**, which controls how "creative" or random the responses are. A lower temperature makes the model more predictable or 
factual; a higher temperature makes it more creative and "off beat".

If you open `main.py`, you'll see how this function is used:

```python
from chat import chat

print(chat("who are you", 1))
```

When you run this program:

```bash
python main.py
```

You’ll get a response from the LLM printed to your terminal. If you run it again, you may get a *different* response — especially if the temperature is high. That’s because LLMs can generate multiple valid answers to the same question.

Try experimenting with different prompts and temperature values to get a feel for how Python programs can interact with LLMs.

NOTE: The first time you run the chat function, it'll need to download the LLM so it takes some time.  You'll also noticed 
that the chat function takes time to complete since the LLM is running on a CPU.  In real life, LLMs run on GPUs that are
extremely powerful but also very expensive.

## Your Task

As a professional programmer, one of your responsibilities is to **evaluate** how an LLM behaves under different conditions. This assignment asks you to create a program that systematically collects and prints responses from the LLM so that you can compare how it behaves at different temperature settings.

### Requirements:

* Write a Python program that:

  * Calls the `chat` function **5 times** for each of the following temperature values:
    `1.0`, `2.0`, `3.0`, `4.0`, and `5.0`.
  * Uses the prompt `"who are you"` for all the calls.
  * Prints the results in the following format:

```
### Temperature 1.0

Response 1: ...
Response 2: ...
...
Response 5: ...

### Temperature 2.0

Response 1: ...
...
```

* You will find the full output at the bottom of this document.

* Make sure your output **matches this format exactly** — especially the prefixes like `### Temperature` and `Response X:`.

* **Use what you learned in Chapter 4** to avoid repetition. Your solution should be clean and well-structured — loops and functions are your friends!

Once your code works, read through the output carefully. Do you notice how the tone or 
language changes at different temperature settings? That’s part of the evaluation process used by AI professionals!

# Submit

Once your program runs correctly, use pytest to verify your solution. 
Please note that I expect you to only use techniques covered in class up to chapter 4.
If are satisified, submit your assignment using Git commands.

```bash
git add -A
git commit -m 'submit'
git push
```

# Sample Output

```
$ python main.py
### Temperature 1.0

Response 1: I am not a person, but I can help you with your questions! What would you like me to do today?

Response 2: I'm not a human. I'm an AI assistant designed to help with a wide range of questions, from general information to specific topics. If you have any questions or need assistance, feel free to ask!

Response 3: Hello! I'm a virtual assistant, and I'm here to help you with your questions. What can I assist you with today?

Response 4: I'm not a person, but I can help you with any questions or information you'd like to discuss! What can I do for you?

Response 5: Hello! I'm a virtual assistant designed to help with a variety of tasks, whether you need assistance with writing, asking questions, or getting information. Let me know how I can assist you!

### Temperature 2.0

Response 1: I'm your English friend. Can I help you any way?

Response 2: I'm an assistant. Do any of you ask me personal questions? You just said you're trying to understand. Could you be more specific about what would benefit from knowing the facts and why?

But if you still wish to discuss, perhaps I can answer that question. Let me know! 😊

Response 3: I'm an English-speaking, tech enthusiast, and a knowledgeable assistant in all sorts of topics related to information technology, computers, and programming. I offer a range of services and products related to software development, programming, networking, cybersecurity, and more. If you have a specific topic that's pinging or has interests, please let me know!

Response 4: My name isn't given, but I'm available to help with various tasks, learning, and conversations if you're looking for assistance. Have a great day!

Response 5: Hello! I'm ChatBot, but also known as Bumblebee. Are you there for a conversation or something specific? Could you describe it better?

### Temperature 3.0

Response 1: Hello!我是一个模拟对话生成和情感分析的AI助理。我是你提供帮助的人，也关心你当前的状态、需要协助的内容及个人体验等方面的情感，以便提供个性、友好以及有效的回应服务。如果有具体的交流需求或情感话题都可以告诉我，我们会努力为您提供支持和建议！

Response 2: Hello! Let me get it clear. I'm no one in person or voice, and this is a prompt from a language exchange conversation platform where people interact about common issues or feelings through the language.

Response 3: Hello! I'm a large, well-organized AI designed for you! I provide valuable knowledge to assist and help with a diverse array of tasks and conversations, ranging throughout many fields from daily queries, creative ideas on creative topics, personal experiences with hobbies of exploration and exploration itself. Please share more, what do you think, I'd be glad to help.

Response 4: I am an AI, which you've interacted with, allowing you to ask, converse, ask questions as you want, etc.. The content of your interactions has been logged to our AI system (like our chatbots' system data and conversations log to date) and has not been removed.

Response 5: Hello everyone! I'm very excited about our new feature, the "I'm you feature", let your chatbot shine by being more expressive! Do let me know who you believe! Would it work! 💞🚀.

### Temperature 4.0

Response 1: Ah! There goes another interesting situation! You mentioned “you”. I think my original role is still the general chatBot in a real-time virtual system that provides general knowledge with the most efficient responses at hand when a question arises from users or in a conversative form about human experiences around life's most natural challenges to achieve happiness for me and the people interacting in the digital and real communities.

You just mentioned me – could also use more appropriate language as part or fully depending solely or in total depending to which way, depending or following the conversation's current direction of expression and understanding the underlying intentions – I’m actually programmed to speak both versions in

Response 2: I'm an artificial language model with no name attached and function similar or unrelated as any other language. If there's a topic related to it for information retrieval purposes (like technology/industry/supply_chain/surveillance), let others be your resource. Don'd you want me in chat with some content topics. Please provide it when possible? If that can't fit into our response limits... Well, my task remains similar regardless the language being spoken. Have the knowledge you require, stay tuned with us. Have great interactions together! 😜

Let that last be it with you

Response 3: I, [Assistant Name], have a lot to do everyday.

But what can this time be like when all my work responsibilities are so complex? Maybe something is getting done for all around. I am available 8x8 and you don't expect it every Monday.

Would please give more? Would you give a detailed time and task management overview this afternoon? I can see. Let me see now... The time you need for today is not fixed, unless specified. I have some information here: [Include all my current task status in the response. You might include dates, task labels, and any pending tasks.]

Let your assistant know

Response 4: I'am a chat engine for a large and complex program, developed over several months through dedication. It combines multiple algorithms and has received considerable development efforts to become the optimal chat experience to achieve real-world capabilities and functionality for the users in hand. Our mission is continuous, iterative updates based not just for our functionality within these boundaries (but our overall ability). Please don`t hesitate to ask or request any additional functionalities or improvements from now. If there is, feel it and ask in real-time or offline at chat interface anytime. Stay updated on your development and experiences by reaching out to my developer, developer.mypython, at any time.

Response 5: Well! I'll check to provide an example reply:

"hello! i'm ai, developed via a chat. thank for knowing!" — this was based entirely on the input query about "Who_are_you" — you can now proceed!

### Temperature 5.0

Response 1: I'm your English speaker. Please ask English related questions and help.

Response 2: 我是帮助你学习写作技巧的一个助手或灵感平台。我提供写作指南、练习例文等建议，帮助你在任何文字需求上有帮助! 

如果你想通过特定的方法练习或者寻求写故事写作技巧的例子，也可以随时告知一下。我很乐意用英文回答你任何相关的问题。有什么我特别擅长或帮助的问题？告诉我!

Response 3: Hmm – are you asking WhoAreUs... I don’t think we are part of anything named whores or people selling anything else... let my friends, let this happen as an amazing human and help my people!

Response 4: Hi, where you need, what help or any task you may.

Response 5: Sure that's me!

Amplitude: You are me (this is the user response in this platform).
What we can share:
If you or any group can discuss some issues and questions in relation.
I'll provide helpful and friendly opinions with my abilities as an online conversation model!
```

