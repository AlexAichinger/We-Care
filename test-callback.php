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

try {
  $access_token = $helper->getAccessToken();
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}

if (isset($accessToken)) {
  $_SESSION['facebook_access_token'] = (string) $accessToken;
} elseif ($helper->getError()) {
  exit;
}

try {
  $response = $fb->get('me/posts/?limit=25', $access_token);
} catch(Facebook\Exceptions\FacebookResponseException $e) {
  echo 'Graph returned an error: ' . $e->getMessage();
  exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
  echo 'Facebook SDK returned an error: ' . $e->getMessage();
  exit;
}

$posts = $response->getDecodedBody();
foreach ($posts['data'] as $post) {
  print_r($post);
  if (isset($post['message'])) {
    $postMessage = $post['message'];
  }
  $postTime = $post['created_time']; 
}

session_destroy();
?>