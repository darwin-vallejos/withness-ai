## Windows PowerShell Encoding Note

Windows PowerShell writes UTF-8 with BOM by default.
Receipt files MUST be written using UTF-8 without BOM.

Approved method:

[System.IO.File]::WriteAllText(
  "receipt.json",
  json_string,
  new UTF8Encoding(false)
)
