#make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
include stdlib

file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^(\s*)IdentityFile',
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^(\s*)PasswordAuthentication',
  ensure => present,
}