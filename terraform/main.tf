provider "yandex" {
  cloud_id  = "b1g33rnkdgjohcdl2ks7"
  folder_id = "b1gjk81mhc94gj788sq9"
  zone      = "ru-central1-a"
}

data "yandex_compute_image" "image" {
  family = "ubuntu-2004-lts"
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

resource "yandex_compute_instance" "test-7-2" {
  name                      = "test-7-2"
  zone                      = "ru-central1-a"
  hostname                  = "test-7-2.netology.cloud"
  allow_stopping_for_update = true

  resources {
    cores  = 2
    memory = 8
  }

  boot_disk {
    initialize_params {
      image_id    = data.yandex_compute_image.image.id
      name        = "root-test-7-2"
      type        = "network-nvme"
      size        = "50"
    }
  }

  network_interface {
    subnet_id = "${yandex_vpc_subnet.default.id}"
    nat       = true
  }

  metadata = {
    ssh-keys = "user:${file("~/.ssh/id_rsa.pub")}"
  }
}
