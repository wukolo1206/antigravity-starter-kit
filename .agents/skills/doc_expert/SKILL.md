# 📄 Word 排版專家手冊 (Custom Skill - @doc_expert)

這是針對 Word 檔案的高級格式自訂排版指南。當用戶在指令中提及 `@doc_expert` 並要求生成 Word 文件時，請主動翻閱本手冊，並在為用戶編寫 python-docx 程式碼時，精確遵循並寫入以下排版規範：

---

## 🎨 格式與排版規約

1. **標題樣式 (Title)**:
   - 字型：`微軟正黑體`
   - 大小：`16 pt`、`粗體 (Bold)`
   - 顏色：`HSL(210, 50%, 30%)` 的高質感深海藍色。

2. **中文段落樣式 (Paragraph)**:
   - 字型：`微軟正黑體`
   - 縮排：段落首行必須自動縮排「兩個中文字元寬度」（首行空兩格）。
   - 對齊：使用兩端對齊（Justified）。

3. **分隔裝飾線 (Decorator Border)**:
   - 在文件的最底端（段落尾部），必須自動繪製一條淺灰色的水平橫線，做為文件結束的視覺分隔。

4. **頁碼自動插入 (Page Numbers)**:
   - 頁尾置中對齊。
   - 自動插入頁碼，字型為 Arial，格式為：`第 X 頁`（如：第 1 頁）。

---

## 🛠️ Python `python-docx` 寫碼引導

- **中文字型與西文字型對齊防線**：
  ```python
  from docx.oxml.ns import qn
  # 設定中文字型
  run.font.name = 'Arial' # 西文
  run._r.get_or_add_rPr().get_or_add_rFonts().set(qn('w:eastAsia'), '微軟正黑體') # 中文
  ```
- **首行縮排**：
  ```python
  from docx.shared import Pt
  p.paragraph_format.first_line_indent = Pt(24) # 縮排
  ```
