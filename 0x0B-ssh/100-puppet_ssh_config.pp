#make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.
include stdlib

file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  require => File['/home/ubuntu/.ssh'],
}

file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
  require => File['/home/ubuntu/.ssh/config'],
}

file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
  require => File['/home/ubuntu/.ssh/config'],
}