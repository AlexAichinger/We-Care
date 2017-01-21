<?php
require_once __DIR__ . '/vendor/autoload.php';

if (!session_id()) {
  session_start();
}

$app_id = 769684356512385;
$app_secret = 'bfafc3ab14067170a74e3977643584f6';

$fb = new Facebook\Facebook([
  'app_id' => $app_id,
  'app_secret' => $app_secret,
  'default_graph_version' => 'v2.8',
  ]);

$helper = $fb->getRedirectLoginHelper();
$permissions = ['user_posts'];
$loginUrl = $helper->getLoginUrl('http://localhost/we-care/test-callback.php', $permissions);

echo '<a href="' . $loginUrl . '">Log in with Facebook!</a>';
?>
