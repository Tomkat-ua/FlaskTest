# Отримуємо назву комп'ютера
$hwid = $env:COMPUTERNAME
$apikey = "abc123"

# Запит до API з HTTP-заголовками
$response = Invoke-RestMethod -Uri "http://your-server-ip:5000/api/data" `
  -Headers @{ "X-API-KEY" = $apikey; "X-HWID" = $hwid } `
  -Method GET

# Вивід результату
$response | ConvertTo-Json -Depth 3
