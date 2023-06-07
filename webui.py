import gradio as gr
import subprocess

#分离人声和背景音乐的音频
def seprateAudio(unseparateAudio):
    subprocess.run([f"demucs {unseparateAudio.name} -o \"output\" -n mdx_extra --two-stems=vocals"], shell=True, check=True)
    return "output/vocals.wav"
#音频切分
def slicerAudio(audio, outdir, db_thresh, min_length, min_interval, hop_size, max_sil_kept):
    subprocess.run(f"python slicer2.py {audio.name} --out {outdir} --db_thresh {db_thresh} --min_length {min_length} --min_interval {min_interval} --hop_size {hop_size} --max_sil_kept {max_sil_kept}", shell=True, check=True)

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Audio Slicer webUI!
    ### 人声背景音乐分离
    """)
    with gr.Row():
        with gr.Column(scale=2):
            unseparateAudio = gr.File(label="输入含背景音乐音频",file_types=['mp3', 'wav', 'wma'], info="输入用于分离人声和背景音乐的音频")
    btnSperate = gr.Button("人声背景音乐分离（分离后音频保存在项目目录下的output/mdx_extra/[音乐名称]/下）")
    gr.Markdown(
    """
    <br/>
    <br/>

    ### 音频切分
    """)
    with gr.Row():
        with gr.Column(scale=2):
            audio = gr.File(label="输入音频",file_types=['mp3', 'wav', 'wma'] ,info="输入用于切分的音频")
            outdir = gr.Textbox(label="输出音频文件目录", value="output", info="输入切分后的音频文件目录路径, 默认为当前目录 output 文件夹")

        with gr.Column(scale=2):
            # sr = gr.Number(label="采样率", value=0, info="音频采样率", precision=0)
            db_thresh = gr.Number(label="RMS阈值", value=-40, precision=0, info="以分贝为单位呈现的RMS阈值。所有RMS值都低于此阈值的区域将被视为静默。如果您的音频嘈杂，请增加此值。默认为-40。")
            min_length = gr.Number(label="最小长度", value=5000, precision=0, info="每个切片音频剪辑所需的最小长度，以毫秒为单位呈现。默认为5000。")
            min_interval = gr.Number(label="静默部分最小长度", value=30, precision=0, info="要切片的静默部分所需的最小长度，以毫秒为单位呈现。如果您的音频仅包含短暂休息时间，则将该值设置得更小。这个数越小，这个脚本生成更多切片后面会产生更多裂变声音效果注意：此值必须比min_length小且大于hop_size 。默认是30。")
            hop_size = gr.Number(label="RMS帧长", value=10, precision=0, info="每个RMS帧长，以毫秒表示。增加此值将提高切割精度，但会减慢过程速度，默认是10.")
            max_sil_kept = gr.Number(label="最长沉默时间", value=1000, precision=0, info="保留在已切割出来声音周围最长沉默时间, 以毫秒表示. 根据需要调整此参数. 注意: 设置该参数并不意味着已经在裁剪出来声音中有完全符合给定长度沉默部分. 算法将搜索最佳位置进行裁剪, 如上所述. 默认为1000.")
    btnSlicer = gr.Button("音频切割")
    btnSperate.click(seprateAudio, inputs=[unseparateAudio])
    btnSlicer.click(slicerAudio, inputs=[audio, outdir, db_thresh, min_length, min_interval, hop_size, max_sil_kept])
    
if __name__ == "__main__":
    # if you run this script locally, it will open a page on your browser
    demo.launch()  