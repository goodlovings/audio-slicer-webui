# 音频切片器

对音频进行切片的 Python 脚本

## 人声和背景音乐分离

使用的是开源的 [demucs](https://github.com/facebookresearch/demucs)

## 安装要求

```shell
pip install -r requirements.txt
```

## 使用

### 使用 webui

```shell
python webui.py
```

然后在浏览器中打开 http://127.0.0.1:7860

### 使用 CLI

脚本可以用 CLI 运行，如下所示:

```bash
python slicer2.py audio[——out out][——db_thresh db_thresh][——min_length min_length][——min_interval min_interval][——hop_size hop_size][——max_sil_keep max_sil_keep]
```

其中' audio '指的是要切片的音频，'——out '默认指向与音频相同的目录，其他选项的默认值如下所示:

#### sr

输入音频的采样率。

#### db_threshold

以分贝为单位呈现的 RMS 阈值。所有 RMS 值都低于此阈值的区域将被视为静默。如果您的音频嘈杂，请增加此值。默认为-40。

#### min_length

每个切片音频剪辑所需的最小长度，以毫秒为单位呈现。默认为 5000。

#### min_interval

要切片的静默部分所需的最小长度，以毫秒为单位呈现。如果您的音频仅包含短暂休息时间，则将该值设置得更小。这个数越小，这个脚本生成更多切片后面会产生更多裂变声音效果注意：此值必须比 min_length 小且大于 hop_size 。默认是 300。

#### hop_size

每个 RMS 帧长，以毫秒表示。增加此值将提高切割精度，但会减慢过程速度，默认是 10.

#### max_silence_kept

保留在已切割出来声音周围最长沉默时间, 以毫秒表示. 根据需要调整此参数. 注意: 设置该参数并不意味着已经在裁剪出来声音中有完全符合给定长度沉默部分. 算法将搜索最佳位置进行裁剪, 如上所述. 默认为 1000.
