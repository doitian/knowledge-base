$title = if ($args.Count -gt 0) {
  $args -join " "
} else {
  Read-Host -Prompt 'title'
}

$tickler = "§ Tickler/Tickler-$($title.Substring(0, 1).ToUpper() -replace '[^A-Z]', '_')"

$dir = "$tickler/$TITLE"
$file = "$dir/♯ $TITLE.md"

mkdir -Force "$dir" | Out-Null

if (-Not (Test-Path -LiteralPath $file)) {
  @(
    "# $title"
  ) | Out-File $file
}

echo "$file"
