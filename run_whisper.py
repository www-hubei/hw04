import whisper
import os

# 1. 加载模型 (base 是平衡速度和准确度的基础模型)
model = whisper.load_model("base")

# 2. 指定你的音频/视频文件路径
audio_path = os.path.join("assets", "jianying_voice.mp4")

print("正在识别中，请稍候...")

# 3. 执行识别
result = model.transcribe(audio_path)

# 4. 打印结果
print("-" * 30)
print("识别结果如下：")
print(result["text"])
print("-" * 30)

# 5. 可选：将识别结果保存到文件
with open("asr_result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])