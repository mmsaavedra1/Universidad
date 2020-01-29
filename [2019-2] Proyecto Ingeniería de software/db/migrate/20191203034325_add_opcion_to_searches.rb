class AddOpcionToSearches < ActiveRecord::Migration[5.2]
  def change
    add_column :searches, :opcion, :integer
  end
end
