class CambiondoNombres2 < ActiveRecord::Migration[5.2]
  def change
    rename_column :restaurantes, :email_admin, :email_propietario
  end
end
