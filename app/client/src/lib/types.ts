export type Group = {
  id: string;
  name: string;
};

export type UserInfo = {
  firstName?: string;
  lastName?: string;
  id: string;
  email: string;
  groups: Group[];
};
