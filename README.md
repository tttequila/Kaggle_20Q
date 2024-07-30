<!-- # Kaggle_20Q
kaggle 20Q noob team from three academic trashes -->

<a href="https://colab.research.google.com/github/tttequila/Kaggle_20Q/blob/main/LLM_Agent.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## 1. Task Description
使用LLMs来进行经典的20 Question游戏，即通过有限问答来猜测出一个对方预先选好的secret word。每次比赛以2v2的形式进行，每队各有两个LLMs，**一个guesser LLM负责根据对方answerer LLM的回答进行提问**，**另一个answerer LLM则负责理解对方队伍的提问并回答yes或者no**。

<details>
        <summary><b> Rules </b></summary>

1. 游戏会被限制在20轮内，超过轮数双方判负
2. 提问限制在2000个字符内
3. 回答限制在100个字符内
4. answerer只能回答yes或者no
5. 任何违规行为直接判负

</details>

<details>
        <summary><b> 资源 </b></summary>

100G disk，16G RAM，T4 GPU

</details>

#### 1.1. Summary
基本上来说，agent需要至少具备两个功能：1. 正确**理解问题**并更具secret word**回答**；2. 根据对方的回答来进行下一个猜测和提问。而根据猜测回答问题则需要agent具有足够的**信息搜集**和**推理能力**

---

## 2. Methodology
<!-- 其实agent的任务本质上是减小下一步的熵（或者是确信度）：作为guesser时，可以是选择能最小化熵的提问方法/secrete word的特征点/etc；而作为answerer时的，这是在yes或者no当中二选一一个置信度最大的选项

而具体怎么实现可能有很多种方法，具体依照game env能提供的游戏信息（例如我们知不知道全部的key words词表）来确定
> 💬
> - 通过**prompting engineering**简单地来选取LLM自己认为置信度最高的特征，回答，猜测，...
> - 通过一些统计上的方法来衡量不确定性
> - 通过一些机器学习的方法来估计一个最大化（最小化）置信度，信息增益，...的选项
>


#### 2.1. KnowNo

那既然都提到了置信度的问题了，刚好可以考虑能不能使用之前面试读到那篇paper，通过一种简单有效的方法来让agent能够自己估计不确定性或者置信度

该文章本质是让robot在实际环境中能够确定有没有歧义的选项，但里面有用到一些比较好用的方法，例如使用多选问题（Multi Choice Question&Answer）来将LLM输出的token的置信度作为这个选项的置信度

至于其具体能否应用进去，可能需要更多的仔细考虑 -->

由于实际比赛中无法获取完整的keyword list，因此基本上LLM是需要具备从零开始规划的能力的，初始化可以从给出的三个categories里面做随机选择，而后面则需要开始根据已知信息进行规划

- **Pure Prompting**: 直接选择比较大的模型进行部署，例如Gemma-9B，然后利用CoT的方法直接得到答案。介于回答时间只有60s，而Gemma-7B *(output_len=100)* 在colab上所需要的推理时间已经高达45s，因此我们只能使用一次prompting来直接生成答案，整不了什么花活
- **CoT Voting**: 考虑到Gemma-2B *(output_len=100)* 的推理速度极快，只需要3s左右即可生成一次response，因此我们可以考虑使用多轮低temperature的采样来生成不同的推理路线，然后再使用投票的方法采样出一个最合适的提问方法

---
<!--
## 3. To-do 📝
暂时来说，目前还在形成思路的阶段，但是有一些东西可以先去了解

- [ ] 怎么部署LLM

> - 这个似乎有很多不同的方法，例如Kaggle似乎原生支持一些合作商的LLM（这里主要是Gemma）的调用，如果我想在自己的环境下测试的话（或者colab环境），可能需要考虑别的方法
> - Kaggle也提供了一些别的LLM，例如Llama 3的各种库的模型实现，并且例如Llama 3，Kaggle也提供了Vertex AI（似乎是Google提供给用户部署LLM的云）的跳转链接。但具体怎么部署还需要自己探索
> - 别的一些开源模型比如Claude等，可以自己获取自己部署
> 
> *但请记住，我们只有16G，应该只能部署一些7B左右的LLM，而且可能需要考虑到会不会有别的小一点的辅助模型需要训练和部署*
- [ ] 思考一下agent的大致框架
- [ ] 看started notebook，对agent的实现有个大概的概念
- [ ] 看论文，或者去搜集别的思路（Chain of Thoughts）来看看能不能达成目标
- [ ] TBC...

---
 -->

## Reference

<details>
        <summary><b> Expand </b></summary>

- KnowNo: https://robot-help.github.io/
- Gemma started notebook: https://www.kaggle.com/code/christianwittmann/llm-20-questions-starter-notebook-fully-documented
- 如何在Kaggle环境部署LLM (video)：https://www.youtube.com/watch?v=jsCUDeg_Op4
- 之前面试用的KnowNo的ppt：https://docs.google.com/presentation/d/180D0WsrutKRSipPYugZ3sYz2Eer1drML/edit?usp=sharing&ouid=116445889014826569768&rtpof=true&sd=true
- 开源LLM汇总：https://www.53ai.com/news/qianyanjishu/1743.html
- Gemma Document: https://ai.google.dev/gemma/docs/pytorch_gemma
- Gemma Cookbook (more details): https://github.com/google-gemini/gemma-cookbook?tab=readme-ov-file
- Advanced Prompting with Gemma: https://github.com/google-gemini/gemma-cookbook/blob/main/Gemma/Advanced_Prompting_Techniques.ipynb
- CoT汇总: https://juejin.cn/post/7204057769493413943
- MoE总结: https://www.53ai.com/news/qianyanjishu/1446.html
- Prompt Engineering Guide: https://www.promptingguide.ai/zh/techniques/tot
- CoT汇总_2: https://zhuanlan.zhihu.com/p/703881352?utm_psn=1797059515520278531
- Discussion on Kaggle
  - Discussion from 1st in public LB: https://www.kaggle.com/competitions/llm-20-questions/discussion/518728
  - started note of Llama-8B: https://www.kaggle.com/code/cdeotte/starter-code-for-llama-8b-llm-lb-0-750
  - Multi-turn QA (paper): https://arxiv.org/abs/2310.01468v3

</details>


![主要看reasoning的指标](imgs/image.png)
<center><i><b> 主要看reasoning的指标 </b></i></center>

----

### To-Do

> ~~总的思路是让agent每次输出都是基于一个选定好的特征来提问（某种程度上，可以类比于一个像random forest的二叉树，只不过不是一个固定好的以及预训练好的树，而是基于LLM的推理和理解和知识注入~~
> 完全通过prompt来激活模型的推理能力，基本上放弃定量分析的思路，只将思路通过CoT prompt来狠狠注入模型😡
>
>     👉直接通过prompting让LLM选择他认为可以最大程度减少不确定性的特征并提问，例如使用CoT等prompting技巧  


- [x] 提交格式
- [ ] 较大模型的单次生成
  - [x] Gemma-7B
  - [ ] Llama-8B
  - [ ] Gemma2-9B
- [ ] 较小模型的多次生成
  - [ ] 多线程同时运行3~4个2B模型最大化时间收益
  - [ ] 通过多轮生成的多步推理来投票出最合适的下一个key attribute