UPDATE users
SET
  `password` = :password,
  needs_password_reset = 0,
  token_expiry_date = null,
  temp_password_token = null
WHERE user_id = :user_id;
