[app]
# App 名稱
title = Strategy2560
# 包名
package.name = strategy2560
# 領域（隨便填 domain）
package.domain = org.example
# 版本號（必填）
version = 1.0.0

# Python 檔案所在資料夾
source.dir = .

# 程式主檔名
source.include_exts = py,png,jpg,kv,txt

# 需求套件
requirements = python3,kivy,pandas,numpy,requests,plyer

# 支援的架構
android.archs = arm64-v8a

# 使用 SDL2 bootstrap
bootstrap = sdl2

# Android 最低 API
android.minapi = 21
# Android target API
android.api = 33

# Debug 模式
log_level = 2
