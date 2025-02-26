require "csv"

module Reporting 
    PROCCESSED_FILE = "data/processed/summary.csv"

    def self.generate_report
        puts "Generating report"

        if !File.exists?(PROCCESSED_FILE)
            puts "File not found"
            return
        end

        csv.foreach(PROCCESSED_FILE, headers: true) do |row|
            puts "Passenger Count: #{row['passenger_count']}, Avg Fare: #{row['avg_fare']}"
        end

        puts "Report generation complete"
    end
end
