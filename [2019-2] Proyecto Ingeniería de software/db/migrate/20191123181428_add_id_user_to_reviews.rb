class AddIdUserToReviews < ActiveRecord::Migration[5.2]
  def change
    add_column :reviews, :id_user, :integer
  end
end
