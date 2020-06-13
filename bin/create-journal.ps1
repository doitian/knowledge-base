$now = Get-Date
$year = $now.Year
$yy   = $now.ToString('yy')
$date = $now.ToString('yyyy-MM-dd')
$dir  = "§ Blog/Journals/Journals - $year/What I Touched This Week $date"
$file = "$dir/♯ What I Touched This Week $date.md"

mkdir -Force "$dir" | Out-Null

if (-Not (Test-Path -LiteralPath $file)) {
  @(
    "---"
    "date: $date"
    "description: My weekly review report."
    "series:"
    "- What I Touched"
    "---"
    ""
    "# What I Touched This Week $date"
  ) | Out-File $file
}

echo "$file"
