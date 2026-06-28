# 🚀 Antigravity 課程懶人包 (Starter Kit)

歡迎使用 **AI Agent 中小學教師行政與備課減量研習** 專用課程懶人包！

本專案是一個特別設計的「初始化環境範本」，旨在透過本機 AI Agent 的自主能力，幫您在 10 秒內搞定所有繁瑣的備課程式安裝與模擬資料庫設定，實現真正「動口不動手」的自動化備課體驗。

---

## 📁 懶人包內容物說明

* 💻 **`index.html`**：研習專屬「一鍵複製 Prompt」主控台（雙擊即可於瀏覽器開啟）。
* 📂 **`cards/`**：預載好各單元實戰所需的模擬 Excel 名冊、自然科教材文字檔及教學 SVG 圖卡。
* 📂 **`google workspace/`**：Google APIs 金鑰與憑證放置位置。
* 📂 **`.agents/`**：大腦自覺引導規則與預裝的 Custom Skills（包含 Word、Excel、PDF 處理專家技能）。

---

## 🛠️ 快速開始使用指南 (學員操作步驟)

### 第一步：載入專案資料夾
1. 打開您的 **Antigravity** 軟體。
2. 點選左側選單的 **New Project** ➔ 選擇 **Add Folder**。
3. 選取本 `antigravity-starter-kit` 資料夾載入。

### 第二步：一鍵完成課程設定 (大腦自動化)
在 Antigravity 對話框中，直接輸入以下指令：
> 💬 **「請幫我完成課程設定。」**

**🎉 接下來，您將親眼見證 Agent 在背景自主完成：**
1. 檢測 Python 執行環境。
2. 自動使用 `pip` 安裝 `python-docx`、`openpyxl` 及 Google APIs 連線套件（請在軟體彈出確認視窗時點選 **`Approve`** 核准）。
3. 檢查您的 Google APIs 憑證狀態。
4. 自動啟用預裝的排版技能包。

### 第三步：放回金鑰 (僅限 Google API 雲端自動化單元)
當您進行到第七與第十單元（雲端簡報與表單自動化）時，請：
1. 將下載好的 Google API 金鑰檔案更名為 **`credentials.json`**。
2. 存放到本專案的 **`google workspace/`** 資料夾底下。
3. 再次呼叫 Agent 執行即可！

---

## 🛡️ 隱私與安全防線
* 本懶人包已內建 `.gitignore` 安全過濾器，您在本機產生的 `token.json` 通行證將會被自動過濾，絕不上傳至公開 Git 倉庫，請放心使用。
