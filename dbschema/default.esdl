
module default {
  abstract type Auditable {
    required property created_at -> datetime {
      readonly := true;
      default := datetime_current();
    }
  }

  type User extending Auditable {
    required property name -> str {
      constraint exclusive;
      constraint max_len_value(50);
    };
  }

  type Event extending Auditable {
    required property name -> str {
      constraint exclusive;
      constraint max_len_value(50);
    }
    property address -> str;
    property schedule -> datetime;
    link host -> User;
  }
}