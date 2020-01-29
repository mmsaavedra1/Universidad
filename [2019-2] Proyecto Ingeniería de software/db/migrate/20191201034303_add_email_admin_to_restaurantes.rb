class AddEmailAdminToRestaurantes < ActiveRecord::Migration[5.2]
  def change
    add_column :restaurantes, :email_admin, :string
  end
end
