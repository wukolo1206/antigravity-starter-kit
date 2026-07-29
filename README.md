# 🚀 Antigravity 課程懶人包 (Starter Kit)

歡迎使用 **AI Agent 中小學教師行政與備課減量研習** 專用課程懶人包！

本專案是一個特別設計的「初始化環境範本」，旨在讓學員親身體驗本機 AI Agent 的自主動手能力（Tool Use）：**只需將 GitHub 官方技能網址丟給 Agent，10 秒內便能自動下載、建立目錄並完成 Skill 技能包安裝！**

---

## 📁 懶人包內容物說明

* 💻 **`index.html`**：研習專屬「一鍵複製 Prompt」主控台（雙擊即可於瀏覽器開啟）。
* 📂 **`cards/`**：預載好各單元實戰所需的模擬 Excel 名冊、自然科教材文字檔及教學圖卡。
* 📂 **`google workspace/`**：Google APIs 金鑰與憑證放置位置（提供簡報與表單自動化實戰）。
* 📂 **`.agents/`**：大腦引導規則與自訂技能基礎目錄。

---

## 🛠️ 快速開始與實戰演練指南

### 第一步：載入專案資料夾
1. 打開您的 **Antigravity** 軟體。
2. 點選左側選單的 **New Project** ➔ 選擇 **Add Folder**。
3. 選取本 `antigravity-starter-kit` 資料夾載入。

### 第二步：環境自動化檢測
在 Antigravity 對話框中，輸入以下指令：
> 💬 **「請幫我完成課程設定。」**
* **Agent 自主動作**：自動檢測 Python 環境，並使用 `pip` 安裝 `python-docx`、`openpyxl` 及 Google APIs 套件。

### 第三步：🌟 重頭戲實戰 —— 命令 Agent 自動安裝 GitHub 官方 Skill！
無需手動開啟瀏覽器下載或手動建立資料夾！直接在對話框貼上 GitHub 官方 Raw 網址：

> 💬 **「請幫我直接下載 GitHub 官方 PDF 技能手冊：  
> https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md  
> 並在我的專案中建立 `.agents/skills/pdf/` 目錄，將該手冊存檔為 `SKILL.md` 安裝進去。完成後回報。」**

🎉 **親眼見證降維打擊**：AI Agent 會在背景自動連網、建立目錄、寫入檔案，瞬間完成技能擴充！

---

## 🛡️ 隱私與安全防線
* 本懶人包已內建 `.gitignore` 安全過濾器，您在本機產生的 `token.json` 通行證將會被自動過濾，絕不上傳至公開 Git 倉庫，請放心使用。
