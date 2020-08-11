# mac 本机
conda activate music

mac 不能安装 spleeter

# 202服务器
conda activate spleeter
cd /home/chenchangshu/spleeter

# 其他
项目根目录下新建pretrained_models/

spleeter separate -i ./wav/fd1f4f0f01bba042579ee1a7de4679e7.wav -p spleeter:2stems -o ./output

# 参考
+ [人声提取工具Spleeter安装教程（Linux）](https://zhuanlan.zhihu.com/p/149944571)
+ [音频处理之人声提取：分离音频背景声，过滤空白](https://zhuanlan.zhihu.com/p/103626813)


aunoise /Users/ccs/Desktop/myRepo/spleeter/fd1f4f0f01bba042579ee1a7de4679e7/vocals.wav ./ [wav]