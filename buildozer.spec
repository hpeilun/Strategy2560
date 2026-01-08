[app]
title = Strategy2560
package.name = strategy2560
package.domain = org.example
version = 1.0.0

# 程式檔案所在資料夾
source.dir = .

# 主程式
source.include_exts = py,kv,png,jpg

# Python 套件
requirements = python3,kivy,pandas,numpy,requests,plyer

# 支援的架構
android.archs = arm64-v8a

# bootstrap
bootstrap = sdl2

# Android API
android.minapi = 21
android.api = 33

# debug 日誌等級
log_level = 2

# 其他設定
android.allow_backup = True
android.permissions = INTERNET
