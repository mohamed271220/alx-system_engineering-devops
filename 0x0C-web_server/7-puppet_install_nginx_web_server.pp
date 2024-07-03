# Puppet manifest to install and configure Nginx with a 301 redirect

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-available/default.erb':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

file_line { 'nginx-redirect':
  path    => '/etc/nginx/sites-available/default',
  line    => '    location /redirect_me { return 301 https://www.example.com/; }',
  match   => '^(\s*)location / {$',
  ensure  => present,
  require => File['/etc/nginx/sites-available/default'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  notify  => Service['nginx'],
}