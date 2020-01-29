class Orden < ApplicationRecord
  belongs_to :plato
  belongs_to :user
end
