output "YC_region" {
  value = "${yandex_compute_instance.test-7-2.zone}"
}

output "Privave_IP" {
  value = "${yandex_compute_instance.test-7-2.network_interface[0].ip_address}"
}

output "Subnet_ID" {
  value = "${yandex_compute_instance.test-7-2.network_interface[0].subnet_id}"
}
