#This puppet script fixes the Word-press site
exec { 'wp_fixer':
  command => 'sed -i s/phpp/phpp/g /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/'
  }