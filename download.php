<?php
$RLO = "\u{202E}";
$PDF = "\u{202C}";

$spoofName = "invoice" . $RLO . "fdp.apk" . $PDF;

header("Content-Type: application/vnd.android.package-archive");
header("Content-Disposition: attachment; filename=\"$spoofName\"");
readfile("test.apk");
