# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2019_12_18_025728) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "favoritos", force: :cascade do |t|
    t.integer "user_id"
    t.integer "restaurante_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "ordens", force: :cascade do |t|
    t.integer "plato_id"
    t.integer "user_id"
    t.integer "precio"
    t.string "direccion_de_envio"
    t.string "estado"
    t.string "notas"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "hora_llegada"
    t.integer "restaurante_id"
  end

  create_table "plato_reviews", force: :cascade do |t|
    t.integer "rating"
    t.text "comentario"
    t.integer "user_id"
    t.integer "plato_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "platos", force: :cascade do |t|
    t.string "nombre"
    t.text "descripcion"
    t.integer "cantidad_personas_sugeridas"
    t.float "valoracion"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "restaurante_id"
    t.string "plato_img_file_name"
    t.string "plato_img_content_type"
    t.bigint "plato_img_file_size"
    t.datetime "plato_img_updated_at"
    t.integer "precio"
  end

  create_table "restaurantes", force: :cascade do |t|
    t.string "nombre"
    t.string "correo"
    t.text "direccion"
    t.float "valoracion"
    t.string "numero_telefono"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "restaurante_img_file_name"
    t.string "restaurante_img_content_type"
    t.bigint "restaurante_img_file_size"
    t.datetime "restaurante_img_updated_at"
  end

  create_table "reviews", force: :cascade do |t|
    t.integer "rating"
    t.text "comentario"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "user_id"
    t.integer "restaurante_id"
  end

  create_table "searches", force: :cascade do |t|
    t.string "keyword"
    t.string "ubicacion"
    t.integer "min_rating"
    t.integer "max_rating"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "opcion"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "nombre"
    t.string "direccion"
    t.string "user_img_file_name"
    t.string "user_img_content_type"
    t.bigint "user_img_file_size"
    t.datetime "user_img_updated_at"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

end
