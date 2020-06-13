$title = if ($args.Count -gt 0) {
  $args -join " "
} else {
  Read-Host -Prompt 'title'
}

$now  = Get-Date
$year = $now.Year
$yy   = $now.ToString('yy')
$mon  = $now.ToString('MM')
$dir  = "§ Blog/Posts/Posts - $year/$yy$mon - $title"
$file = "$dir/♯ $TITLE.md"

mkdir -Force "$dir" | Out-Null

if (-Not (Test-Path -LiteralPath $file)) {
  @(
    "---"
    "date: '$($now.ToString('o'))'"
    "draft: true"
    "---"
    ""
    "# $title"
  ) | Out-File $file
}

echo "$file"
