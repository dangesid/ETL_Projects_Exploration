require 'rake'
require_relative 'lib/data_ingestion'
require_relative 'lib/reporting'

namespace :etl do
    desc "Check dataset availability"
    task :fetch do
        DataIngestion.fetch_data
    end

    desc "Process dataset using PySpark"
    task :process do
        sh "python3 scripts/process_data.py"
    end

    desc "Generate report from processed_data"
    task :report do
        Reporting.generate_report
    end

    desc "Run full ETL pipeline"
    task all: [:fetch, :process, :report]

end