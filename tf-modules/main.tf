provider "yandex" {
  cloud_id  = "b1g33rnkdgjohcdl2ks7"
  folder_id = "b1gjk81mhc94gj788sq9"
  zone      = "ru-central1-a"
}

resource "yandex_vpc_network" "default" {
  name = "net"
}

resource "yandex_vpc_subnet" "default" {
  name           = "subnet"
  zone           = "ru-central1-a"
  network_id     = "${yandex_vpc_network.default.id}"
  v4_cidr_blocks = ["192.168.101.0/24"]
}

module "sandryunin_instance" {
  source = "./modules/instance"
  instance_count = 3

  subnet_id     = "${yandex_vpc_subnet.default.id}"
  zone          = "ru-central1-a"
  folder_id     = "b1gjk81mhc94gj788sq9"
  image         = "ubuntu-2004-lts"
  platform_id   = "standard-v1"
  name          = "instance"
  cores         = "2"
  boot_disk     = "network-nvme"
  disk_size     = "50"
  nat           = "true"
  memory        = "4"
  core_fraction = "100"
}
