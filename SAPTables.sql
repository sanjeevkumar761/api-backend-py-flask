
/*******************************************************************************
   SAP Database - Version 1.4
   Script: SAPTables.sql
   Description: Creates and populates the SAP database.
   DB Server: Sqlite
********************************************************************************/

/*******************************************************************************
   Drop Foreign Keys Constraints
********************************************************************************/





















/*******************************************************************************
   Drop Tables
********************************************************************************/
DROP TABLE IF EXISTS [SalesOrders];

/*******************************************************************************
   Create Tables
********************************************************************************/
CREATE TABLE [SalesOrders]
(
    [ID] NVARCHAR(160)  NOT NULL,
    [SalesOrder] NVARCHAR(160)  NOT NULL,
    [SalesOrder_Text] NVARCHAR(160)  NOT NULL, 
    [CreatedByUser] NVARCHAR(160)  NOT NULL,
    [CreationDateTime] NVARCHAR(160)  NOT NULL,
    [Customer] NVARCHAR(160)  NOT NULL, 
    [TransactionCurrency] NVARCHAR(160)  NOT NULL, 
    [GrossAmountInTransacCurrency] NVARCHAR(160)  NOT NULL, 
    [SalesOrderOverallStatus] NVARCHAR(160)  NOT NULL
);


/*******************************************************************************
   Create Primary Key Unique Indexes
********************************************************************************/

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/

/*******************************************************************************
   Populate Tables
********************************************************************************/
INSERT INTO [SalesOrders] ([ID], [SalesOrder], [SalesOrder_Text], [CreatedByUser], [CreationDateTime], [Customer], [TransactionCurrency], [GrossAmountInTransacCurrency], [SalesOrderOverallStatus]) VALUES ('.1~0500000000', '500000000', 'EPM DG: SO ID 0500000000 Deliver as fast as possible', 'EPM_DEMO', '2017-12-31 23:00:00+00:00', '100000000', 'USD', '14385.85', 'Open');
INSERT INTO [SalesOrders] ([ID], [SalesOrder], [SalesOrder_Text], [CreatedByUser], [CreationDateTime], [Customer], [TransactionCurrency], [GrossAmountInTransacCurrency], [SalesOrderOverallStatus]) VALUES ('.1~0500000001', '500000001', 'DBG: Deliver only in last week of month', 'DBG_DEMO', '2018-01-07T23:00:00.0000000Z', '100000002', 'USD', '15117.76', 'Closed');
