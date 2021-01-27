provider "google" {
    project = "ingka-cybersec-gkesec-test"
    region  = "us-central1"
    zone    = "us-central1-c"
}

resource "google_storage_bucket" "bucket" {
    name    = "terraform-rw-poc-bucket"
}

resource "google_storage_bucket_access_control" "public_rule" {
    bucket  = "terraform-rw-poc-bucket"
    role    = "READER"
    entity  = "allUsers"
}

resource "google_sql_database_instance" "master" {
    name                = "master-instance"
    database_version    = "POSTGRES_11"
    region              = "us-central1"

    settings {
        tier = "db-f1-micro"
    }
}