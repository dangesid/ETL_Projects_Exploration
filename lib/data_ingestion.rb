require 'fileutils'

module DataIngestion
    FILE_NAME = "data/raw/2018_Yellow_Taxi_Trip_Data_20250226.csv"

    def self.fetch_data
        file_path = "#{FILE_NAME}"

        if File.exist?(file_path)
            puts "dataset is already present in the path"
        else
            puts "Error: CSV file NOT found in #{FILE_NAME}. Please add the dataset"

        end
    end
end