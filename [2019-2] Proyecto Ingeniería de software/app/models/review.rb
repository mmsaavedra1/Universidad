class Review < ApplicationRecord
  belongs_to :restaurante
  belongs_to :user
end
