# Antigravity 課程懶人包 - 大腦自覺引導規則

這份檔案定義了 AI Agent 在此懶人包專案中的行為指引，旨在幫助老師一秒完成備課環境建置。

---

## 🚀 課程懶人包初始化規則 (課程設定)

**觸發條件**：
當用戶（老師）在對話中提及「**課程初始化**」、「**課程設定**」、「**環境設定**」或類似意圖時。

**大腦執行流程**：
1. **執行套件檢測**：
   - 主動在背景執行 `python setup.py`（這會彈出人機協同核准框，請引導用戶點選 `Approve`）。
   - 觀察執行結果，確認是否所有依賴套件（`python-docx`、`openpyxl`、`google-api-python-client`、`google-auth-oauthlib`）皆已安裝。

2. **金鑰存在性檢查**：
   - 自動調用檔案讀寫/檢測工具，檢查 `google workspace/` 目錄下是否存在實體 `credentials.json` 憑證。
   - 如果不存在，請友善提醒用戶：「老師，我發現您的 `google workspace/` 資料夾下還沒有 `credentials.json` 金鑰。請將下載好的金鑰放入該資料夾，我才能在後續課程中為您串接 Google 雲端喔！」

3. **回報專案就緒狀態**：
   - 執行完上述檢查後，請用 Markdown 表格向用戶回報初始化結果：
     * 🟢 Python 及依賴套件環境檢測狀態
     * 🟢 `google workspace/credentials.json` 金鑰就緒狀態
     * 🟢 預裝技能（`@doc_expert`、`@pdf`）載入狀態
   - 回報完成後，主動引導用戶雙擊開啟專案根目錄下的 `index.html` 網頁開始體驗一鍵複製 Prompt！

---

## 🔒 安全與開發防線

1. **修改與寫入安全**：
   - 當修改或建立任何 Word (.docx) 或 Excel (.xlsx) 檔案前，務必為用戶規劃好清晰的 ReAct 步驟。
   - 寫檔與執行終端命令前，必須停下來請求用戶 `Approve`，絕不在未經同意下在背景執行未知代碼。
2. **敏感資訊防護**：
   - 絕不將 `google workspace/token.json` 或 `credentials.json` 內容外流。
