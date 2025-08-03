# �������� ����� ����'�����
$hwid = $env:COMPUTERNAME
$apikey = "abc123"

# ����� �� API � HTTP-�����������
$response = Invoke-RestMethod -Uri "http://your-server-ip:5000/api/data" `
  -Headers @{ "X-API-KEY" = $apikey; "X-HWID" = $hwid } `
  -Method GET

# ���� ����������
$response | ConvertTo-Json -Depth 3
