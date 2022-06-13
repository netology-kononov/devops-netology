**1. Вывод команды terraform workspace list.**
```commandline
ubun@mscn:~/netology/devops-netology/terraform$ terraform workspace list
  default
* prod
  stage
```

**2. Вывод команды terraform plan для воркспейса prod.**
```commandline
ubun@mscn:~/netology/devops-netology/terraform$ terraform plan
data.yandex_compute_image.image: Reading...
data.yandex_compute_image.image: Read complete after 0s [id=fd8mn5e1cksb3s1pcq12]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_instance.test-7-3[0] will be created
  + resource "yandex_compute_instance" "test-7-3" {
      + allow_stopping_for_update = true
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + hostname                  = "test-7-3-0.netology.cloud"
      + id                        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                user:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCx55pgg5e8LcFmHbUDsmdi9Tq+KY6xZhKxUcZnkASGnu92BwafhY/LTQQp7I3Vit2IiSSKlIPcM6jP3MJkyy6QiQV+VqKazXjLHy9vKUwgEqwejHacmkhCSCGxPsIQFv6xQ2tScsM1DBZhtn5xrtRoEh31pkHUyCrHZHUU81AbNnoJc8dNn3+PtEYyngLqPu1UoGGVDz2gI7HRzhgJ9+T08iNYjerXEPyByrZNcJqf7sJNLDvL5DBmf9vNen2hlu2vYe0PQfE2GUfKSMGDSXAJFrudByotN5EwixrgOYNKBU6WwvuaQl3SqVDDfOcG6G+P0q5lh14lxrtcM4RWNs/f2DikHV6FWXxVSA5FJiq65AB8jsxFtrxSkgemuqkha4W0/GxHV+FKjvP2t8UfjjylZgJDMkzGcyOplRXLyKS2Uf+yZOiWsHmPaMH5BBqZR4XmA3FEq2geUQ46CAqFvAUmAs3phfRzTuVXYj75HOsDyRr4eGSAWOrt+LUKTmaG4F0= ubun@mscn
            EOT
        }
      + name                      = "test-7-3-0"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8mn5e1cksb3s1pcq12"
              + name        = "root-test-7-3-0"
              + size        = 50
              + snapshot_id = (known after apply)
              + type        = "network-nvme"
            }
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy {
          + host_affinity_rules = (known after apply)
          + placement_group_id  = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 8
        }

      + scheduling_policy {
          + preemptible = (known after apply)
        }
    }

  # yandex_compute_instance.test-7-3[1] will be created
  + resource "yandex_compute_instance" "test-7-3" {
      + allow_stopping_for_update = true
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + hostname                  = "test-7-3-1.netology.cloud"
      + id                        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                user:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCx55pgg5e8LcFmHbUDsmdi9Tq+KY6xZhKxUcZnkASGnu92BwafhY/LTQQp7I3Vit2IiSSKlIPcM6jP3MJkyy6QiQV+VqKazXjLHy9vKUwgEqwejHacmkhCSCGxPsIQFv6xQ2tScsM1DBZhtn5xrtRoEh31pkHUyCrHZHUU81AbNnoJc8dNn3+PtEYyngLqPu1UoGGVDz2gI7HRzhgJ9+T08iNYjerXEPyByrZNcJqf7sJNLDvL5DBmf9vNen2hlu2vYe0PQfE2GUfKSMGDSXAJFrudByotN5EwixrgOYNKBU6WwvuaQl3SqVDDfOcG6G+P0q5lh14lxrtcM4RWNs/f2DikHV6FWXxVSA5FJiq65AB8jsxFtrxSkgemuqkha4W0/GxHV+FKjvP2t8UfjjylZgJDMkzGcyOplRXLyKS2Uf+yZOiWsHmPaMH5BBqZR4XmA3FEq2geUQ46CAqFvAUmAs3phfRzTuVXYj75HOsDyRr4eGSAWOrt+LUKTmaG4F0= ubun@mscn
            EOT
        }
      + name                      = "test-7-3-1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8mn5e1cksb3s1pcq12"
              + name        = "root-test-7-3-1"
              + size        = 50
              + snapshot_id = (known after apply)
              + type        = "network-nvme"
            }
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy {
          + host_affinity_rules = (known after apply)
          + placement_group_id  = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 8
        }

      + scheduling_policy {
          + preemptible = (known after apply)
        }
    }

  # yandex_compute_instance.test-7-3-foreach["standard-v1"] will be created
  + resource "yandex_compute_instance" "test-7-3-foreach" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + hostname                  = "test-7-3-standard-v1.netology.cloud"
      + id                        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                user:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCx55pgg5e8LcFmHbUDsmdi9Tq+KY6xZhKxUcZnkASGnu92BwafhY/LTQQp7I3Vit2IiSSKlIPcM6jP3MJkyy6QiQV+VqKazXjLHy9vKUwgEqwejHacmkhCSCGxPsIQFv6xQ2tScsM1DBZhtn5xrtRoEh31pkHUyCrHZHUU81AbNnoJc8dNn3+PtEYyngLqPu1UoGGVDz2gI7HRzhgJ9+T08iNYjerXEPyByrZNcJqf7sJNLDvL5DBmf9vNen2hlu2vYe0PQfE2GUfKSMGDSXAJFrudByotN5EwixrgOYNKBU6WwvuaQl3SqVDDfOcG6G+P0q5lh14lxrtcM4RWNs/f2DikHV6FWXxVSA5FJiq65AB8jsxFtrxSkgemuqkha4W0/GxHV+FKjvP2t8UfjjylZgJDMkzGcyOplRXLyKS2Uf+yZOiWsHmPaMH5BBqZR4XmA3FEq2geUQ46CAqFvAUmAs3phfRzTuVXYj75HOsDyRr4eGSAWOrt+LUKTmaG4F0= ubun@mscn
            EOT
        }
      + name                      = "test-7-3-standard-v1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8mn5e1cksb3s1pcq12"
              + name        = "root-test-7-3-standard-v1"
              + size        = 50
              + snapshot_id = (known after apply)
              + type        = "network-nvme"
            }
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy {
          + host_affinity_rules = (known after apply)
          + placement_group_id  = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 8
        }

      + scheduling_policy {
          + preemptible = (known after apply)
        }
    }

  # yandex_compute_instance.test-7-3-foreach["standard-v2"] will be created
  + resource "yandex_compute_instance" "test-7-3-foreach" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + hostname                  = "test-7-3-standard-v2.netology.cloud"
      + id                        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                user:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCx55pgg5e8LcFmHbUDsmdi9Tq+KY6xZhKxUcZnkASGnu92BwafhY/LTQQp7I3Vit2IiSSKlIPcM6jP3MJkyy6QiQV+VqKazXjLHy9vKUwgEqwejHacmkhCSCGxPsIQFv6xQ2tScsM1DBZhtn5xrtRoEh31pkHUyCrHZHUU81AbNnoJc8dNn3+PtEYyngLqPu1UoGGVDz2gI7HRzhgJ9+T08iNYjerXEPyByrZNcJqf7sJNLDvL5DBmf9vNen2hlu2vYe0PQfE2GUfKSMGDSXAJFrudByotN5EwixrgOYNKBU6WwvuaQl3SqVDDfOcG6G+P0q5lh14lxrtcM4RWNs/f2DikHV6FWXxVSA5FJiq65AB8jsxFtrxSkgemuqkha4W0/GxHV+FKjvP2t8UfjjylZgJDMkzGcyOplRXLyKS2Uf+yZOiWsHmPaMH5BBqZR4XmA3FEq2geUQ46CAqFvAUmAs3phfRzTuVXYj75HOsDyRr4eGSAWOrt+LUKTmaG4F0= ubun@mscn
            EOT
        }
      + name                      = "test-7-3-standard-v2"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8mn5e1cksb3s1pcq12"
              + name        = "root-test-7-3-standard-v2"
              + size        = 50
              + snapshot_id = (known after apply)
              + type        = "network-nvme"
            }
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + placement_policy {
          + host_affinity_rules = (known after apply)
          + placement_group_id  = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 4
          + memory        = 8
        }

      + scheduling_policy {
          + preemptible = (known after apply)
        }
    }

  # yandex_vpc_network.default will be created
  + resource "yandex_vpc_network" "default" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "net"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.default will be created
  + resource "yandex_vpc_subnet" "default" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.101.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 6 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + Privave_IP = [
      + (known after apply),
      + (known after apply),
    ]
  + Subnet_ID  = [
      + (known after apply),
      + (known after apply),
    ]
  + YC_region  = [
      + "ru-central1-a",
      + "ru-central1-a",
    ]
```
