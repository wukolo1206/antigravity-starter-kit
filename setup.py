import sys
import subprocess

# 解決 Windows 控制台 Emoji 輸出 cp950 編碼崩潰的問題
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

required_libraries = [
    "python-docx",
    "openpyxl",
    "google-api-python-client",
    "google-auth-oauthlib"
]

def check_and_install():
    print("📢 [Antigravity Starter Kit] 開始進行環境與套件依賴檢測...")
    print(f"🐍 當前 Python 執行環境: {sys.executable}")
    
    missing = []
    for lib in required_libraries:
        # 對於名稱不一致的套件進行處理（如 python-docx 載入為 docx）
        import_name = lib
        if lib == "python-docx":
            import_name = "docx"
        elif lib == "google-api-python-client":
            import_name = "googleapiclient"
        elif lib == "google-auth-oauthlib":
            import_name = "google_auth_oauthlib"
            
        try:
            __import__(import_name)
            print(f"🟢 套件已存在: {lib}")
        except ImportError:
            missing.append(lib)
            print(f"🟡 套件缺失: {lib}")
            
    if missing:
        print(f"\n⚙️ 發現缺漏的必要依賴: {missing}")
        print("🚀 準備自動呼叫 pip 安裝中，請稍候...")
        try:
            # 呼叫 pip 安裝缺失依賴
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + missing)
            print("🟢 所有依賴套件均已順利安裝完成！")
        except Exception as e:
            print(f"❌ 套件安裝失敗，錯誤原因: {e}")
            print("💡 建議提示：若是學校學術網路 (TANet) 阻擋，請手動確認網路連線或使用手機熱點連網後再試。")
            sys.exit(1)
    else:
        print("\n🎉 恭喜！本機環境完全就緒，已安裝所有備課所需的第三方套件！")

if __name__ == "__main__":
    check_and_install()
